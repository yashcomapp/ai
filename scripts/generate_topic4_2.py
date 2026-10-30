# scripts/generate_topic4_2.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-4-4.2"
CHAPTER_NUM = 4

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Atomic size and nanometer scale
    ("""What physical dimension determines the size of an atom?""",
     ["Atomic mass",
      "Atomic radius (the distance between the nucleus of the atom and its outermost electron shell)",
      "Number of neutrons in the nucleus",
      "Total density of the nucleus"],
     "B", "OSC", "easy",
     "• The size of an atom is defined by its atomic radius, which is the distance from the central nucleus to the outermost electron orbit.\nCorrect Choice is (B)."),

    ("""Atomic radius is typically expressed in which unit of measurement?""",
     ["Millimetre (\\(\\text{mm}\\))", "Micrometre (\\(\\mu\\text{m}\\))", "Nanometre (\\(\\text{nm}\\))", "Centimetre (\\(\\text{cm}\\))"],
     "C", "OSC", "easy",
     "• Because atoms are unimaginably tiny, atomic radius is measured in nanometres (\\(\\text{nm}\\)), where \\(1\\text{ nm} = 10^{-9}\\text{ m}\\).\nCorrect Choice is (C)."),

    ("""What is the relationship between \\(1\\text{ metre}\\) and \\(1\\text{ nanometre}\\)?""",
     ["\\(1\\text{ m} = 10^6\\text{ nm}\\)",
      "\\(1\\text{ nm} = 10^{-9}\\text{ m}\\ (\\text{or } 1\\text{ m} = 10^9\\text{ nm})\\)",
      "\\(1\\text{ nm} = 10^{-6}\\text{ m}\\)",
      "\\(1\\text{ nm} = 10^{-12}\\text{ m}\\)"],
     "B", "OSC", "easy",
     "• \\(1\\text{ nanometre} = 10^{-9}\\text{ metre}\\), or \\(1\\text{ m} = 10^9\\text{ nm}\\).\nCorrect Choice is (B)."),

    ("""What is the approximate atomic radius of a Hydrogen atom?""",
     ["\\(10^{-4}\\text{ m}\\)", "\\(10^{-6}\\text{ m}\\)", "\\(10^{-8}\\text{ m}\\)", "\\(10^{-10}\\text{ m}\\) (or \\(0.1\\text{ nm}\\))"],
     "D", "OSC", "easy",
     "• A hydrogen atom is the smallest atom with an atomic radius of approximately \\(10^{-10}\\text{ m} = 0.1\\text{ nm}\\).\nCorrect Choice is (D)."),

    ("""What is the approximate size (diameter/radius) of a water molecule (\\(\\text{H}_2\\text{O}\\))?""",
     ["\\(10^{-3}\\text{ m}\\)", "\\(10^{-6}\\text{ m}\\)", "\\(10^{-9}\\text{ m}\\) (or \\(1\\text{ nm}\\))", "\\(10^{-12}\\text{ m}\\)"],
     "C", "OSC", "easy",
     "• A water molecule has dimensions of order \\(10^{-9}\\text{ m} = 1\\text{ nm}\\).\nCorrect Choice is (C)."),

    ("""As one moves from LEFT to RIGHT across a period in the Modern Periodic Table, what happens to atomic radius?""",
     ["Atomic radius increases continuously",
      "Atomic radius decreases because positive nuclear charge increases while electrons enter the same valence shell, pulling electrons closer to the nucleus",
      "Atomic radius remains strictly constant",
      "Atomic radius first doubles then drops to zero"],
     "B", "OSC", "medium",
     "• Moving left to right across a period, atomic number increases so nuclear charge pulls electrons tighter within the same shell, shrinking atomic radius.\nCorrect Choice is (B)."),

    ("""As one moves DOWN a group (from top to bottom) in the Periodic Table, what happens to atomic radius?""",
     ["Atomic radius decreases",
      "Atomic radius increases because a new electron shell is added with each successive period, placing valence electrons farther from the nucleus",
      "Atomic radius remains identical",
      "Atomic radius oscillates randomly"],
     "B", "OSC", "medium",
     "• Going down a group, the addition of new electron shells increases the distance between the nucleus and the valence shell, increasing atomic size.\nCorrect Choice is (B)."),

    ("""Which of the following elements has the LARGEST atomic radius?""",
     ["Lithium (\\(\\text{Li}\\))", "Sodium (\\(\\text{Na}\\))", "Potassium (\\(\\text{K}\\))", "Rubidium (\\(\\text{Rb}\\))"],
     "D", "OSC", "medium",
     "• Down Group 1 (\\(\\text{Li} < \\text{Na} < \\text{K} < \\text{Rb}\\)), atomic radius increases with each additional electron shell; \\(\\text{Rb}\\) has the largest radius among these.\nCorrect Choice is (D)."),

    ("""Which of the following atoms in the second period has the SMALLEST atomic radius?""",
     ["Lithium (\\(\\text{Li}\\))", "Carbon (\\(\\text{C}\\))", "Oxygen (\\(\\text{O}\\))", "Fluorine (\\(\\text{F}\\))"],
     "D", "OSC", "medium",
     "• Across Period 2 from left to right, atomic radius decreases; Fluorine has the greatest effective nuclear charge pulling its 2nd shell inward, giving it the smallest radius.\nCorrect Choice is (D)."),

    ("""What is the approximate size of a human red blood cell (RBC) compared to an atom?""",
     ["\\(10^{-10}\\text{ m}\\) (same as atom)",
      "\\(10^{-6}\\text{ m}\\) (\\(\\sim 10{,}000\\) times larger than an atom)",
      "\\(10^{-2}\\text{ m}\\)",
      "\\(1\\text{ m}\\)"],
     "B", "OSC", "medium",
     "• A red blood cell is about \\(7\\text{ to }8\\,\\mu\\text{m} = 10^{-6}\\text{ m}\\), roughly \\(10{,}000\\) to \\(100{,}000\\) times larger than a single atom.\nCorrect Choice is (B)."),

    # 11-20: Atomic Mass Unit and C-12 standard
    ("""Why was the mass of an atom traditionally determined as a 'relative' mass rather than an absolute mass in grams?""",
     ["Because ancient scientists had no balance scales",
      "Because an individual atom is unimaginably tiny (mass \\(\\sim 10^{-24}\\text{ g}\\)), making absolute measurement impossible until modern mass spectrometry",
      "Because atoms lose mass when touched",
      "Because atomic mass changes every hour"],
     "B", "OSC", "easy",
     "• Individual atoms have minute masses (e.g. hydrogen \\(\\approx 1.66 \\times 10^{-24}\\text{ g}\\)), so scientists used relative comparisons to a chosen reference standard.\nCorrect Choice is (B)."),

    ("""Which isotope is universally accepted by the IUPAC as the standard reference for atomic mass units since 1961?""",
     ["Hydrogen-1 (\\(^1\\text{H}\\))",
      "Oxygen-16 (\\(^{16}\\text{O}\\))",
      "Carbon-12 (\\(^{12}\\text{C}\\))",
      "Nitrogen-14 (\\(^{14}\\text{N}\\))"],
     "C", "OSC", "easy",
     "• Carbon-12 is the international standard, assigned an atomic mass of exactly \\(12\\text{ u}\\).\nCorrect Choice is (C)."),

    ("""What is the precise definition of one unified atomic mass unit (\\(1\\text{ u}\\) or Dalton)?""",
     ["The mass of one hydrogen atom",
      "Exactly \\(\\frac{1}{12}\\text{th}\\) of the mass of one neutral Carbon-12 (\\(^{12}\\text{C}\\)) atom",
      "\\(\\frac{1}{16}\\text{th}\\) of an oxygen atom",
      "The mass of one electron"],
     "B", "OSC", "easy",
     "• \\(1\\text{ u} = \\frac{1}{12}\\) the mass of a single \\(^{12}\\text{C}\\) atom \\(\\approx 1.6605 \\times 10^{-27}\\text{ kg}\\).\nCorrect Choice is (B)."),

    ("""What is the mass of \\(1\\text{ Dalton (u)}\\) expressed in kilograms?""",
     ["\\(1.6605 \\times 10^{-24}\\text{ kg}\\)",
      "\\(1.6605 \\times 10^{-27}\\text{ kg}\\)",
      "\\(9.109 \\times 10^{-31}\\text{ kg}\\)",
      "\\(6.022 \\times 10^{-23}\\text{ kg}\\)"],
     "B", "OSC", "medium",
     "• \\(1\\text{ u} = 1.6605 \\times 10^{-27}\\text{ kg} = 1.6605 \\times 10^{-24}\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""What is the relative atomic mass of Sodium (\\(\\text{Na}\\)) in unified atomic mass units (\\(\\text{u}\\))?""",
     ["\\(11\\text{ u}\\)", "\\(23\\text{ u}\\)", "\\(24\\text{ u}\\)", "\\(40\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Sodium has atomic number 11 (11 protons, 12 neutrons) and atomic mass \\(23\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""What is the relative atomic mass of Chlorine (\\(\\text{Cl}\\)) taking into account its natural isotopic abundances (\\(^{35}\\text{Cl}\\) and \\(^{37}\\text{Cl}\\))?""",
     ["\\(35.0\\text{ u}\\)", "\\(35.5\\text{ u}\\)", "\\(36.0\\text{ u}\\)", "\\(37.0\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Chlorine exists naturally as \\(75\\%\\ ^{35}\\text{Cl}\\) and \\(25\\%\\ ^{37}\\text{Cl}\\), yielding an average atomic mass of \\(0.75(35) + 0.25(37) = 35.5\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""Which scientist proposed the modern method of representing chemical elements using one or two letters derived from their name?""",
     ["John Dalton", "Jöns Jacob Berzelius", "Dmitri Mendeleev", "Robert Boyle"],
     "B", "OSC", "easy",
     "• Swedish chemist J. J. Berzelius suggested that elemental symbols be derived from the first letter (capital) and/or second letter of the element name.\nCorrect Choice is (B)."),

    ("""What is the Latin name from which the chemical symbol for Potassium (\\(\\text{K}\\)) is derived?""",
     ["Kalium", "Natrium", "Plumbum", "Cuprum"],
     "A", "OSC", "easy",
     "• Potassium is \\(\\text{K}\\) from Latin 'Kalium'.\nCorrect Choice is (A)."),

    ("""What is the Latin name and chemical symbol for Lead?""",
     ["Ferrum, \\(\\text{Fe}\\)", "Plumbum, \\(\\text{Pb}\\)", "Argentum, \\(\\text{Ag}\\)", "Stannum, \\(\\text{Sn}\\)"],
     "B", "OSC", "easy",
     "• Lead is \\(\\text{Pb}\\) from Latin 'Plumbum'.\nCorrect Choice is (B)."),

    ("""What are the chemical symbols for Gold and Silver, respectively?""",
     ["\\(\\text{Go}\\) and \\(\\text{Si}\\)",
      "\\(\\text{Au}\\) (Aurum) and \\(\\text{Ag}\\) (Argentum)",
      "\\(\\text{Gd}\\) and \\(\\text{Sv}\\)",
      "\\(\\text{Al}\\) and \\(\\text{Sr}\\)"],
     "B", "OSC", "easy",
     "• Gold is \\(\\text{Au}\\) (Aurum) and Silver is \\(\\text{Ag}\\) (Argentum).\nCorrect Choice is (B)."),

    # 21-30: Valency and valence electrons
    ("""What is meant by the 'VALENCY' of an element?""",
     ["The number of neutrons in its nucleus",
      "The combining capacity of an atom of an element to form chemical bonds",
      "The boiling point of the element",
      "The total number of protons and electrons"],
     "B", "OSC", "easy",
     "• Valency is the combining capacity of an atom, determined by the number of valence electrons given, taken, or shared to achieve a stable octet/duplet.\nCorrect Choice is (B)."),

    ("""How is valency related to the number of valence electrons for elements whose valence shell has 1, 2, 3, or 4 electrons?""",
     ["\\(\\text{Valency} = 8 - \\text{valence electrons}\\)",
      "\\(\\text{Valency} = \\text{valence electrons}\\)",
      "\\(\\text{Valency} = 2 \\times \\text{valence electrons}\\)",
      "Valency is always zero"],
     "B", "OSC", "easy",
     "• For 1 to 4 valence electrons, the atom easily loses or shares these electrons, so valency equals the number of valence electrons.\nCorrect Choice is (B)."),

    ("""What is the valency of an element whose neutral atom has the electronic configuration \\(2, 8, 7\\) (Chlorine)?""",
     ["7", "1", "8", "2"],
     "B", "OSC", "easy",
     "• With 7 valence electrons, chlorine needs \\(8 - 7 = 1\\) electron to complete its octet; hence its valency is 1.\nCorrect Choice is (B)."),

    ("""What is the valency of Magnesium (atomic number 12, electronic configuration \\(2, 8, 2\\))?""",
     ["1", "2", "6", "8"],
     "B", "OSC", "easy",
     "• Magnesium readily loses its 2 valence electrons to achieve the stable neon octet \\(2, 8\\); its valency is 2.\nCorrect Choice is (B)."),

    ("""What is the valency of noble gases such as Helium, Neon, and Argon?""",
     ["8", "2", "0", "1"],
     "C", "OSC", "easy",
     "• Noble gases have completely filled valence shells (duplet for He, octet for Ne, Ar), so they do not combine; their valency is 0.\nCorrect Choice is (C)."),

    ("""Assertion (A): Across a period from Sodium (Na) to Chlorine (Cl), the atomic radius decreases continuously.\nReason (R): As the atomic number increases across the period, the positive nuclear charge pulls the electrons in the third shell closer to the nucleus.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "• Nuclear charge increases from +11 in Na to +17 in Cl within the same principle quantum shell \\(n=3\\), drawing the shell closer and decreasing atomic radius.\nCorrect Choice is (A)."),

    ("""Assertion (A): The atomic mass of an atom is almost entirely concentrated in its nucleus.\nReason (R): The mass of an electron is negligible (\\(\\approx \\frac{1}{1837}\\text{th}\\) of a proton mass), while protons and neutrons in the nucleus carry virtually all the atomic mass.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Protons and neutrons (nucleons) account for \\(> 99.95\\%\\) of total atomic mass, since electron mass is negligible.\nCorrect Choice is (A)."),

    ("""State True or False: Variable valency is exhibited by transition metals like Iron (\\(\\text{Fe}^{2+}\\) ferrous and \\(\\text{Fe}^{3+}\\) ferric) and Copper (\\(\\text{Cu}^+\\) cuprous and \\(\\text{Cu}^{2+}\\) cupric).""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Transition metals can lose electrons from penultimate inner shells as well as valence shells, displaying variable valencies.\nCorrect Choice is (A)."),

    ("""State True or False: One Dalton is exactly equivalent to one gram.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. \\(1\\text{ Dalton} = 1.6605 \\times 10^{-24}\\text{ g}\\); it is \\(6.022 \\times 10^{23}\\) times smaller than one gram.\nCorrect Choice is (B)."),

    ("""Which element has the Latin name 'Stannum' and chemical symbol \\(\\text{Sn}\\)?""",
     ["Silver", "Strontium", "Tin", "Antimony"],
     "C", "OSC", "easy",
     "• Tin has Latin name Stannum (\\(\\text{Sn}\\)).\nCorrect Choice is (C)."),

    # 31-40: Fill in blanks, molecular mass calculations
    ("""Fill in the blank: The unit of atomic mass is symbolized as ________, which stands for unified mass (Dalton).""",
     ["\\(\\text{kg}\\)", "\\(\\text{u}\\)", "\\(\\text{mol}\\)", "\\(\\text{amu}^2\\)"],
     "B", "OFB", "easy",
     "• The unified atomic mass unit is symbolized by 'u' (Dalton, Da).\nCorrect Choice is (B)."),

    ("""Fill in the blank: \\(1\\text{ metre} = 10^9\\) ________.""",
     ["Picometres", "Nanometres", "Centimetres", "Micrometres"],
     "B", "OFB", "easy",
     "• \\(1\\text{ m} = 10^9\\text{ nm}\\).\nCorrect Choice is (B)."),

    ("""What is the molecular mass of a water molecule (\\(\\text{H}_2\\text{O}\\))? (Given atomic masses: \\(\\text{H}=1\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(17\\text{ u}\\)", "\\(18\\text{ u}\\)", "\\(20\\text{ u}\\)", "\\(34\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Molecular mass = \\((2 \\times 1) + 16 = 18\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""What is the molecular mass of carbon dioxide (\\(\\text{CO}_2\\))? (Given: \\(\\text{C}=12\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(28\\text{ u}\\)", "\\(44\\text{ u}\\)", "\\(32\\text{ u}\\)", "\\(56\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Molecular mass = \\(12 + (2 \\times 16) = 12 + 32 = 44\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""Calculate the formula unit mass of Calcium Carbonate (\\(\\text{CaCO}_3\\)). (Given: \\(\\text{Ca}=40\\text{ u}\\), \\(\\text{C}=12\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(68\\text{ u}\\)", "\\(84\\text{ u}\\)", "\\(100\\text{ u}\\)", "\\(112\\text{ u}\\)"],
     "C", "OSC", "easy",
     "• Mass = \\(40 + 12 + (3 \\times 16) = 40 + 12 + 48 = 100\\text{ u}\\).\nCorrect Choice is (C)."),

    ("""What is the molecular mass of Sulphuric Acid (\\(\\text{H}_2\\text{SO}_4\\))? (Given: \\(\\text{H}=1\\text{ u}\\), \\(\\text{S}=32\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(49\\text{ u}\\)", "\\(98\\text{ u}\\)", "\\(82\\text{ u}\\)", "\\(100\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\((2 \\times 1) + 32 + (4 \\times 16) = 2 + 32 + 64 = 98\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""What is the valency of Carbon (atomic number 6, electronic configuration \\(2, 4\\))?""",
     ["2", "3", "4 (tetravalent)", "6"],
     "C", "OSC", "easy",
     "• Carbon shares 4 valence electrons to complete its octet, making it tetravalent (valency 4).\nCorrect Choice is (C)."),

    ("""An atom \\(X\\) has electronic configuration \\(2, 8, 3\\). What is the valency of element \\(X\\) and to which group does it belong?""",
     ["Valency 3, Group 13 (Aluminium)",
      "Valency 5, Group 15",
      "Valency 1, Group 1",
      "Valency 2, Group 2"],
     "A", "OSC", "medium",
     "• Electronic configuration \\(2, 8, 3\\) corresponds to Aluminium (atomic number 13). Valency is 3, belonging to Group 13.\nCorrect Choice is (A)."),

    ("""What is the Latin name and symbol for Mercury?""",
     ["Hydrargyrum, \\(\\text{Hg}\\)", "Natrium, \\(\\text{Na}\\)", "Kalium, \\(\\text{K}\\)", "Argentum, \\(\\text{Ag}\\)"],
     "A", "OSC", "easy",
     "• Mercury is Hydrargyrum (\\(\\text{Hg}\\), meaning liquid silver).\nCorrect Choice is (A)."),

    ("""Which subatomic particles are collectively called 'nucleons'?""",
     ["Electrons and Protons", "Protons and Neutrons", "Electrons and Neutrons", "Protons and Positrons"],
     "B", "OSC", "easy",
     "• Particles residing inside the atomic nucleus (protons and neutrons) are called nucleons.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What is \\(1\\text{ nanometre}\\) in metres?""",
     ["\\(10^{-3}\\text{ m}\\)", "\\(10^{-6}\\text{ m}\\)", "\\(10^{-9}\\text{ m}\\)", "\\(10^{-12}\\text{ m}\\)"],
     "C", "OSC", "easy",
     "• \\(1\\text{ nm} = 10^{-9}\\text{ m}\\).\nCorrect Choice is (C)."),

    ("""Which is the smallest atom among all elements?""",
     ["Helium", "Hydrogen", "Lithium", "Carbon"],
     "B", "OSC", "easy",
     "• Hydrogen has the smallest atomic radius (\\(\\approx 10^{-10}\\text{ m}\\)).\nCorrect Choice is (B)."),

    ("""The atomic mass of Carbon-12 is taken as exactly:""",
     ["\\(1\\text{ u}\\)", "\\(6\\text{ u}\\)", "\\(12\\text{ u}\\)", "\\(14\\text{ u}\\)"],
     "C", "OSC", "easy",
     "• Standard \\(^{12}\\text{C}\\) has an atomic mass of exactly \\(12\\text{ u}\\).\nCorrect Choice is (C)."),

    ("""What is the valency of Aluminium (\\(\\text{Al}\\), atomic number 13)?""",
     ["1", "2", "3", "4"],
     "C", "OSC", "easy",
     "• Aluminium configuration is \\(2, 8, 3\\); valency is 3.\nCorrect Choice is (C)."),

    ("""What is the valency of Oxygen (atomic number 8, configuration \\(2, 6\\))?""",
     ["6", "2", "8", "4"],
     "B", "OSC", "easy",
     "• Valency = \\(8 - 6 = 2\\).\nCorrect Choice is (B)."),

    ("""What is the symbol for Sodium derived from its Latin name Natrium?""",
     ["\\(\\text{So}\\)", "\\(\\text{Sd}\\)", "\\(\\text{Na}\\)", "\\(\\text{Nt}\\)"],
     "C", "OSC", "easy",
     "• Sodium is \\(\\text{Na}\\) from Natrium.\nCorrect Choice is (C)."),

    ("""What is the symbol for Iron derived from Latin Ferrum?""",
     ["\\(\\text{Ir}\\)", "\\(\\text{Fe}\\)", "\\(\\text{Fr}\\)", "\\(\\text{In}\\)"],
     "B", "OSC", "easy",
     "• Iron is \\(\\text{Fe}\\) from Ferrum.\nCorrect Choice is (B)."),

    ("""What is the symbol for Copper derived from Latin Cuprum?""",
     ["\\(\\text{Cp}\\)", "\\(\\text{Co}\\)", "\\(\\text{Cu}\\)", "\\(\\text{Cr}\\)"],
     "C", "OSC", "easy",
     "• Copper is \\(\\text{Cu}\\) from Cuprum.\nCorrect Choice is (C)."),

    ("""What is the molecular mass of Sodium Chloride (\\(\\text{NaCl}\\))? (Given: \\(\\text{Na}=23\\text{ u}\\), \\(\\text{Cl}=35.5\\text{ u}\\))""",
     ["\\(58.5\\text{ u}\\)", "\\(46.0\\text{ u}\\)", "\\(55.0\\text{ u}\\)", "\\(71.0\\text{ u}\\)"],
     "A", "OSC", "easy",
     "• Mass = \\(23 + 35.5 = 58.5\\text{ u}\\).\nCorrect Choice is (A)."),

    ("""What is the molecular mass of Ammonia (\\(\\text{NH}_3\\))? (Given: \\(\\text{N}=14\\text{ u}\\), \\(\\text{H}=1\\text{ u}\\))""",
     ["\\(15\\text{ u}\\)", "\\(16\\text{ u}\\)", "\\(17\\text{ u}\\)", "\\(18\\text{ u}\\)"],
     "C", "OSC", "easy",
     "• Mass = \\(14 + (3 \\times 1) = 17\\text{ u}\\).\nCorrect Choice is (C)."),

    ("""What is the molecular mass of Nitric Acid (\\(\\text{HNO}_3\\))? (Given: \\(\\text{H}=1\\text{ u}\\), \\(\\text{N}=14\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(48\\text{ u}\\)", "\\(63\\text{ u}\\)", "\\(64\\text{ u}\\)", "\\(70\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\(1 + 14 + (3 \\times 16) = 15 + 48 = 63\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""The valency of an element having electronic configuration \\(2, 8, 5\\) (Phosphorus) is:""",
     ["5", "3", "8", "2"],
     "B", "OSC", "medium",
     "• Phosphorus can accept/share 3 electrons (\\(8 - 5 = 3\\)); it also exhibits variable valency 3 and 5.\nCorrect Choice is (B)."),

    ("""What is the valency of Calcium (atomic number 20, electronic configuration \\(2, 8, 8, 2\\))?""",
     ["1", "2", "4", "8"],
     "B", "OSC", "easy",
     "• Valency of Calcium is 2.\nCorrect Choice is (B)."),

    ("""Why do all noble gases have valency zero?""",
     ["They have no electrons",
      "Their valence shell is completely filled (duplet/octet), so they have zero tendency to gain, lose, or share electrons",
      "Their atomic mass is zero",
      "They are radioactive"],
     "B", "OSC", "easy",
     "• Completely filled outermost shells confer extreme stability, resulting in zero chemical valency.\nCorrect Choice is (B)."),

    ("""Which element exhibits variable valencies of 1 and 2?""",
     ["Copper (\\(\\text{Cu}^+, \\text{Cu}^{2+}\\))", "Magnesium", "Aluminium", "Sodium"],
     "A", "OSC", "medium",
     "• Copper forms Cuprous (valency 1) and Cupric (valency 2) compounds.\nCorrect Choice is (A)."),

    ("""Which element exhibits variable valencies of 2 and 3?""",
     ["Iron (\\(\\text{Fe}^{2+}, \\text{Fe}^{3+}\\))", "Zinc", "Calcium", "Potassium"],
     "A", "OSC", "medium",
     "• Iron forms Ferrous (valency 2) and Ferric (valency 3).\nCorrect Choice is (A)."),

    ("""What is the formula unit mass of Potassium Hydroxide (\\(\\text{KOH}\\))? (Given: \\(\\text{K}=39\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\), \\(\\text{H}=1\\text{ u}\\))""",
     ["\\(55\\text{ u}\\)", "\\(56\\text{ u}\\)", "\\(57\\text{ u}\\)", "\\(60\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\(39 + 16 + 1 = 56\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""What is the molecular mass of Glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\))? (Given: \\(\\text{C}=12\\text{ u}\\), \\(\\text{H}=1\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(160\\text{ u}\\)", "\\(180\\text{ u}\\)", "\\(192\\text{ u}\\)", "\\(200\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\((6 \\times 12) + (12 \\times 1) + (6 \\times 16) = 72 + 12 + 96 = 180\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""What is the molecular mass of Sucrose (Cane sugar, \\(\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}\\))? (Given: \\(\\text{C}=12\\text{ u}\\), \\(\\text{H}=1\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(342\\text{ u}\\)", "\\(360\\text{ u}\\)", "\\(330\\text{ u}\\)", "\\(354\\text{ u}\\)"],
     "A", "OSC", "medium",
     "• Mass = \\((12 \\times 12) + (22 \\times 1) + (11 \\times 16) = 144 + 22 + 176 = 342\\text{ u}\\).\nCorrect Choice is (A)."),

    ("""How many electrons are in the outermost shell of a halogen atom (Group 17)?""",
     ["1", "5", "7", "8"],
     "C", "OSC", "easy",
     "• Halogens (F, Cl, Br, I) have 7 valence electrons and valency 1.\nCorrect Choice is (C)."),

    ("""What is the Latin name and symbol for Potassium?""",
     ["Natrium, \\(\\text{Na}\\)", "Kalium, \\(\\text{K}\\)", "Ferrum, \\(\\text{Fe}\\)", "Stibium, \\(\\text{Sb}\\)"],
     "B", "OSC", "easy",
     "• Potassium is Kalium (\\(\\text{K}\\)).\nCorrect Choice is (B)."),

    ("""State True or False: Across Period 3 from Na to Ar, the number of electron shells increases from 1 to 3.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. All elements in Period 3 have exactly 3 electron shells; electrons enter the 3rd shell progressively.\nCorrect Choice is (B)."),

    ("""State True or False: Down Group 1 from Li to Cs, the number of electron shells increases by 1 for each successive period.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Li has 2 shells, Na has 3, K has 4, Rb has 5, Cs has 6.\nCorrect Choice is (A)."),

    ("""What is the formula unit mass of Magnesium Oxide (\\(\\text{MgO}\\))? (Given: \\(\\text{Mg}=24\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(32\\text{ u}\\)", "\\(40\\text{ u}\\)", "\\(48\\text{ u}\\)", "\\(56\\text{ u}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\(24 + 16 = 40\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""What is the formula unit mass of Aluminium Oxide (\\(\\text{Al}_2\\text{O}_3\\))? (Given: \\(\\text{Al}=27\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\))""",
     ["\\(54\\text{ u}\\)", "\\(102\\text{ u}\\)", "\\(88\\text{ u}\\)", "\\(118\\text{ u}\\)"],
     "B", "OSC", "medium",
     "• Mass = \\((2 \\times 27) + (3 \\times 16) = 54 + 48 = 102\\text{ u}\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The Latin name for Antimony from which its symbol \\(\\text{Sb}\\) is taken is ________.""",
     ["Stannum", "Stibium", "Silicium", "Scandium"],
     "B", "OFB", "easy",
     "• Antimony is Stibium (\\(\\text{Sb}\\)).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The Latin name for Tungsten from which its chemical symbol \\(\\text{W}\\) is taken is ________.""",
     ["Wolfram", "Natrium", "Plumbum", "Cuprum"],
     "A", "OFB", "easy",
     "• Tungsten is Wolfram (\\(\\text{W}\\)).\nCorrect Choice is (A)."),

    ("""What is the valency of Silicon (atomic number 14, configuration \\(2, 8, 4\\))?""",
     ["2", "3", "4", "8"],
     "C", "OSC", "easy",
     "• Silicon shares 4 valence electrons; its valency is 4.\nCorrect Choice is (C)."),

    ("""Which element has the largest atomic size in Period 3?""",
     ["Sodium (\\(\\text{Na}\\))", "Magnesium (\\(\\text{Mg}\\))", "Chlorine (\\(\\text{Cl}\\))", "Argon (\\(\\text{Ar}\\))"],
     "A", "OSC", "medium",
     "• In Period 3, Sodium has the fewest nuclear protons (+11) pulling its 3rd shell, giving it the largest atomic radius in the period.\nCorrect Choice is (A)."),

    ("""What is the mass of one single Carbon-12 atom in grams?""",
     ["\\(1.9926 \\times 10^{-23}\\text{ g}\\)",
      "\\(1.6605 \\times 10^{-24}\\text{ g}\\)",
      "\\(12\\text{ g}\\)",
      "\\(6.022 \\times 10^{-23}\\text{ g}\\)"],
     "A", "OSC", "medium",
     "• \\(\\text{Mass} = 12 \\times 1.6605 \\times 10^{-24} \\approx 1.9926 \\times 10^{-23}\\text{ g}\\).\nCorrect Choice is (A).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Nanometer Dimension Scale Ladder
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Logarithmic Scale of Relative Sizes</text>
  <!-- Scale Bar -->
  <line x1="40" y1="180" x2="300" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <!-- H Atom: 10^-10 m -->
  <circle cx="60" cy="120" r="4" fill="#38bdf8"/>
  <line x1="60" y1="130" x2="60" y2="180" stroke="#475569" stroke-width="1.5"/>
  <text x="40" y="105" fill="#38bdf8" font-size="9" font-weight="bold">Hydrogen Atom</text>
  <text x="45" y="198" fill="#94a3b8" font-size="9">10⁻¹⁰ m</text>
  <!-- Water Molecule: 10^-9 m -->
  <circle cx="120" cy="115" r="7" fill="#60a5fa"/>
  <line x1="120" y1="130" x2="120" y2="180" stroke="#475569" stroke-width="1.5"/>
  <text x="100" y="98" fill="#60a5fa" font-size="9" font-weight="bold">H₂O Molecule</text>
  <text x="110" y="198" fill="#94a3b8" font-size="9">10⁻⁹ m (1 nm)</text>
  <!-- Haemoglobin: 10^-8 m -->
  <circle cx="180" cy="110" r="12" fill="#ef4444"/>
  <line x1="180" y1="130" x2="180" y2="180" stroke="#475569" stroke-width="1.5"/>
  <text x="155" y="88" fill="#f87171" font-size="9" font-weight="bold">Haemoglobin</text>
  <text x="170" y="198" fill="#94a3b8" font-size="9">10⁻⁸ m</text>
  <!-- Red Blood Cell: 10^-6 m -->
  <circle cx="260" cy="95" r="22" fill="#dc2626"/>
  <line x1="260" y1="130" x2="260" y2="180" stroke="#475569" stroke-width="1.5"/>
  <text x="240" y="65" fill="#fca5a5" font-size="9" font-weight="bold">Red Blood Cell</text>
  <text x="250" y="198" fill="#94a3b8" font-size="9">10⁻⁶ m</text>
</svg>
</div>
In the comparative dimensional scale diagram above, how many times larger in diameter is a typical human Red Blood Cell (\\(10^{-6}\\text{ m}\\)) compared to an individual Hydrogen atom (\\(10^{-10}\\text{ m}\\))?""",
     ["\\(10\\) times", "\\(100\\) times", "\\(10{,}000\\) times (\\(10^4\\) times)", "\\(10^8\\) times"],
     "C", "OSC", "medium",
     "• Ratio of sizes = \\(\\frac{10^{-6}\\text{ m}}{10^{-10}\\text{ m}} = 10^4 = 10{,}000\\) times larger.\nCorrect Choice is (C)."),

    # 502: Carbon-12 Standard Reference Wedge
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">The Carbon-12 Standard (1 Dalton)</text>
  <!-- Pie showing 12 equal slices -->
  <circle cx="120" cy="115" r="60" fill="#1e293b" stroke="#475569" stroke-width="2"/>
  <!-- Highlighted 1/12th slice -->
  <path d="M 120 115 L 120 55 A 60 60 0 0 1 150 63 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
  <text x="90" y="120" fill="#cbd5e1" font-size="9">¹²C Atom</text>
  <text x="80" y="135" fill="#94a3b8" font-size="8">(Mass = 12 u)</text>
  <!-- Pointer to 1/12 slice -->
  <line x1="140" y1="50" x2="210" y2="70" stroke="#f59e0b" stroke-width="2"/>
  <rect x="210" y="55" width="115" height="50" fill="#334155" stroke="#f59e0b" rx="4"/>
  <text x="215" y="75" fill="#fde047" font-size="10" font-weight="bold">1 u (1 Dalton)</text>
  <text x="215" y="90" fill="#cbd5e1" font-size="8">= 1/12th of ¹²C mass</text>
  <text x="215" y="100" fill="#cbd5e1" font-size="8">≈ 1.6605 × 10⁻²⁷ kg</text>
  <text x="45" y="195" fill="#34d399" font-size="10">International standard established by IUPAC in 1961</text>
</svg>
</div>
The figure illustrates the unified atomic mass standard. If the absolute mass of one Carbon-12 atom is \\(1.9926 \\times 10^{-23}\\text{ g}\\), what is the mass of \\(1\\text{ u}\\) (one unified atomic mass unit) in grams?""",
     ["\\(1.9926 \\times 10^{-24}\\text{ g}\\)",
      "\\(1.6605 \\times 10^{-24}\\text{ g}\\)",
      "\\(1.2000 \\times 10^{-23}\\text{ g}\\)",
      "\\(0.1660 \\times 10^{-24}\\text{ g}\\)"],
     "B", "OSC", "medium",
     "• \\(1\\text{ u} = \\frac{1.9926 \\times 10^{-23}\\text{ g}}{12} \\approx 1.6605 \\times 10^{-24}\\text{ g}\\).\nCorrect Choice is (B)."),

    # 503: Atomic Radius Definition
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="95" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Atomic Radius Definition</text>
  <!-- Nucleus -->
  <circle cx="170" cy="115" r="16" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="155" y="120" fill="#fff" font-size="10" font-weight="bold">+Ze</text>
  <!-- Shell 1 (K) -->
  <circle cx="170" cy="115" r="38" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- Shell 2 (L - Valence shell) -->
  <circle cx="170" cy="115" r="65" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Valence electron -->
  <circle cx="235" cy="115" r="5" fill="#fde047"/>
  <text x="245" y="118" fill="#fde047" font-size="9">e⁻</text>
  <!-- Radius Dimension Line -->
  <line x1="170" y1="115" x2="235" y2="115" stroke="#10b981" stroke-width="2.5"/>
  <text x="185" y="105" fill="#34d399" font-size="11" font-weight="bold">r (radius)</text>
  <text x="40" y="195" fill="#cbd5e1" font-size="10">Distance between nucleus centre and outermost electron shell</text>
</svg>
</div>
In the atomic structure model above, which factor causes atomic radius to DECREASE as you move from Sodium (atomic number 11) to Chlorine (atomic number 17) across Period 3?""",
     ["Electrons are lost to outer space",
      "Nuclear charge increases from +11 to +17 while electrons fill the same valence shell (n=3), pulling all electrons closer to the nucleus with greater electrostatic attraction",
      "Neutrons push the nucleus outward",
      "Mass of protons decreases"],
     "B", "OSC", "hard",
     "• Across a period, positive nuclear charge increases while principal quantum shell remains identical, generating stronger attraction that contracts the electron cloud.\nCorrect Choice is (B)."),

    # 504: Periodic Table Atomic Size Trends
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Periodic Trends in Atomic Size</text>
  <!-- Across Period Arrow (Left to Right) -->
  <line x1="50" y1="70" x2="270" y2="70" stroke="#ef4444" stroke-width="3"/>
  <polygon points="275,70 265,65 265,75" fill="#ef4444"/>
  <text x="60" y="60" fill="#f87171" font-size="10" font-weight="bold">Across Period (→): Atomic Radius DECREASES</text>
  <text x="60" y="90" fill="#cbd5e1" font-size="9">• Increasing nuclear pull on same valence shell</text>
  <!-- Down Group Arrow (Top to Bottom) -->
  <line x1="70" y1="110" x2="70" y2="190" stroke="#10b981" stroke-width="3"/>
  <polygon points="70,195 65,185 75,185" fill="#10b981"/>
  <text x="90" y="135" fill="#34d399" font-size="10" font-weight="bold">Down Group (↓): Atomic Radius INCREASES</text>
  <text x="90" y="155" fill="#cbd5e1" font-size="9">• New electron shells are added with each row</text>
  <text x="90" y="175" fill="#cbd5e1" font-size="9">• Shielding effect increases</text>
</svg>
</div>
Based on the periodic trend vector diagram, which of the following elements has the SMALLEST atomic radius?""",
     ["Potassium (\\(\\text{K}\\))", "Sodium (\\(\\text{Na}\\))", "Chlorine (\\(\\text{Cl}\\))", "Rubidium (\\(\\text{Rb}\\))"],
     "C", "OSC", "hard",
     "• Sodium and Chlorine are in Period 3; atomic size decreases across a period, making Chlorine smaller than Sodium. Potassium and Rubidium are below Sodium with more shells, making them much larger. Hence, Chlorine has the smallest radius.\nCorrect Choice is (C)."),

    # 505: Electronic Configuration & Valency (Na & Cl)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Electron Transfer &amp; Valency</text>
  <!-- Sodium Box -->
  <rect x="25" y="50" width="135" height="100" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="72" fill="#38bdf8" font-size="11" font-weight="bold">Sodium (Na: Z=11)</text>
  <text x="35" y="92" fill="#cbd5e1" font-size="10">EC: (2, 8, 1)</text>
  <text x="35" y="112" fill="#fde047" font-size="10">Loses 1 e⁻ → Na⁺ (2,8)</text>
  <text x="35" y="135" fill="#34d399" font-size="11" font-weight="bold">Valency = 1</text>
  <!-- Chlorine Box -->
  <rect x="180" y="50" width="135" height="100" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="190" y="72" fill="#10b981" font-size="11" font-weight="bold">Chlorine (Cl: Z=17)</text>
  <text x="190" y="92" fill="#cbd5e1" font-size="10">EC: (2, 8, 7)</text>
  <text x="190" y="112" fill="#fde047" font-size="10">Gains 1 e⁻ → Cl⁻ (2,8,8)</text>
  <text x="190" y="135" fill="#34d399" font-size="11" font-weight="bold">Valency = 8 - 7 = 1</text>
  <!-- Arrow -->
  <text x="65" y="185" fill="#93c5fd" font-size="10">Both achieve inert noble gas electronic configuration</text>
</svg>
</div>
In the electronic configurations shown, why do Sodium and Chlorine BOTH have a valency of 1, despite Sodium having 1 valence electron and Chlorine having 7 valence electrons?""",
     ["Because they have the same atomic mass",
      "Because Sodium achieves an octet by losing 1 electron, while Chlorine achieves an octet by gaining 1 electron; valency represents the number of electrons exchanged to achieve octet stability",
      "Because Chlorine can donate 7 electrons easily",
      "Because valency is always 1 for all elements"],
     "B", "OSC", "medium",
     "• Valency measures combining capacity. Sodium loses 1 electron (valency 1), and Chlorine gains 1 electron (\\(8 - 7 = 1\\), valency 1).\nCorrect Choice is (B)."),

    # 506: Water Molecular Mass Computation Tree
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Molecular Mass Computation: H₂SO₄</text>
  <!-- Elements breakdown -->
  <text x="30" y="60" fill="#cbd5e1" font-size="11">• 2 atoms of Hydrogen: 2 × 1 u = 2 u</text>
  <text x="30" y="90" fill="#cbd5e1" font-size="11">• 1 atom of Sulphur: 1 × 32 u = 32 u</text>
  <text x="30" y="120" fill="#cbd5e1" font-size="11">• 4 atoms of Oxygen: 4 × 16 u = 64 u</text>
  <line x1="30" y1="135" x2="310" y2="135" stroke="#475569" stroke-width="1.5"/>
  <rect x="30" y="150" width="280" height="40" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="45" y="175" fill="#38bdf8" font-size="12" font-weight="bold">Total Molecular Mass = 2 + 32 + 64 = 98 u</text>
</svg>
</div>
Following the molecular mass computation method for sulphuric acid shown above, what is the formula unit mass of Calcium Hydroxide (\\(\\text{Ca(OH)}_2\\))? (Given: \\(\\text{Ca}=40\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\), \\(\\text{H}=1\\text{ u}\\))""",
     ["\\(57\\text{ u}\\)", "\\(74\\text{ u}\\)", "\\(98\\text{ u}\\)", "\\(114\\text{ u}\\)"],
     "B", "OSC", "medium",
     "• Formula unit mass = \\(40 + 2 \\times (16 + 1) = 40 + 34 = 74\\text{ u}\\).\nCorrect Choice is (B)."),

    # 507: Variable Valency (Iron Fe2+ vs Fe3+)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Variable Valency of Iron (Fe)</text>
  <!-- Ferrous Box -->
  <rect x="30" y="55" width="130" height="90" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="40" y="80" fill="#34d399" font-size="11" font-weight="bold">Ferrous Ion (Fe²⁺)</text>
  <text x="40" y="100" fill="#cbd5e1" font-size="10">• Valency: 2</text>
  <text x="40" y="118" fill="#cbd5e1" font-size="10">• e.g. FeCl₂ (Greenish)</text>
  <text x="40" y="135" fill="#94a3b8" font-size="9">Iron(II) chloride</text>
  <!-- Ferric Box -->
  <rect x="180" y="55" width="130" height="90" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="190" y="80" fill="#fde047" font-size="11" font-weight="bold">Ferric Ion (Fe³⁺)</text>
  <text x="190" y="100" fill="#cbd5e1" font-size="10">• Valency: 3</text>
  <text x="190" y="118" fill="#cbd5e1" font-size="10">• e.g. FeCl₃ (Brownish)</text>
  <text x="190" y="135" fill="#94a3b8" font-size="9">Iron(III) chloride</text>
  <text x="40" y="185" fill="#93c5fd" font-size="10">Suffix '-ous' denotes lower valency; '-ic' denotes higher valency</text>
</svg>
</div>
What causes certain transition metals like Iron to display variable valency (both \\(\\text{Fe}^{2+}\\) and \\(\\text{Fe}^{3+}\\)) in chemical compounds?""",
     ["Their nuclei lose protons during reactions",
      "Electrons from the penultimate (second from outside) d-shell can be lost along with outer valence s-electrons under different reaction conditions",
      "The atoms split into smaller isotopes",
      "They absorb photons to create extra positive charge"],
     "B", "OSC", "hard",
     "• In transition elements like iron (\\(3d^6 4s^2\\)), loss of only the two \\(4s\\) electrons yields \\(\\text{Fe}^{2+}\\), while losing an additional \\(3d\\) electron yields a stable half-filled \\(3d^5\\) configuration (\\(\\text{Fe}^{3+}\\)).\nCorrect Choice is (B)."),

    # 508: Berzelius Elemental Symbolism Historical Evolution
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Evolution of Chemical Symbols</text>
  <!-- Dalton's Pictorial Symbols -->
  <rect x="30" y="50" width="130" height="80" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <text x="40" y="70" fill="#e2e8f0" font-size="10" font-weight="bold">Dalton's Symbols</text>
  <circle cx="55" cy="95" r="10" fill="none" stroke="#fde047" stroke-width="2"/>
  <circle cx="55" cy="95" r="3" fill="#fde047"/>
  <text x="75" y="100" fill="#cbd5e1" font-size="9">Hydrogen ⊙</text>
  <!-- Berzelius Letter System -->
  <rect x="180" y="50" width="130" height="80" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="190" y="70" fill="#38bdf8" font-size="10" font-weight="bold">Berzelius System</text>
  <text x="195" y="100" fill="#38bdf8" font-size="16" font-weight="bold">H, O, C, Na</text>
  <text x="190" y="118" fill="#cbd5e1" font-size="9">Letter of element name</text>
  <text x="40" y="165" fill="#fde047" font-size="10" font-weight="bold">Rule: First letter CAPITAL, second letter LOWERCASE</text>
  <text x="40" y="190" fill="#94a3b8" font-size="9">e.g. Cobalt is Co (element), whereas CO is carbon monoxide (compound)</text>
</svg>
</div>
Why was Berzelius's alphabetical nomenclature adopted internationally over Dalton's pictorial symbols?""",
     ["Because pictorial symbols were impossible to print on early printing presses and became confusing as hundreds of compounds were discovered",
      "Because Berzelius was the King of Sweden",
      "Because letters do not occupy any physical space",
      "Because Dalton's symbols were written in Greek"],
     "A", "OSC", "medium",
     "• Dalton's complex circles and geometric glyphs were cumbersome to draw and print, whereas standardized single- and two-letter abbreviations (Berzelius) enabled unambiguous global communication.\nCorrect Choice is (A)."),

    # 509: Cobalt (Co) vs Carbon Monoxide (CO) Case Sensitivity
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Case Sensitivity in Chemical Symbols</text>
  <!-- Cobalt -->
  <rect x="30" y="55" width="130" height="85" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="75" y="90" fill="#38bdf8" font-size="24" font-weight="bold">Co</text>
  <text x="45" y="115" fill="#93c5fd" font-size="10">Pure Metallic Element</text>
  <text x="45" y="130" fill="#cbd5e1" font-size="9">(Cobalt, Atomic No. 27)</text>
  <!-- Carbon Monoxide -->
  <rect x="180" y="55" width="130" height="85" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="220" y="90" fill="#ef4444" font-size="24" font-weight="bold">CO</text>
  <text x="195" y="115" fill="#fca5a5" font-size="10">Chemical Compound</text>
  <text x="195" y="130" fill="#cbd5e1" font-size="9">(Carbon + Oxygen, toxic gas)</text>
  <text x="45" y="180" fill="#fde047" font-size="10" font-weight="bold">Writing 'CO' instead of 'Co' changes an element into a toxic gas!</text>
</svg>
</div>
What critical rule of chemical notation does the difference between 'Co' and 'CO' demonstrate?""",
     ["Chemical symbols have no capitalization rules",
      "When an elemental symbol has two letters, the first must be capitalized and the second strictly lowercase; two consecutive capital letters indicate a chemical compound formed from two distinct elements",
      "Cobalt and Carbon Monoxide are isotopes of each other",
      "Lowercase letters can be used anywhere in formulas"],
     "B", "OSC", "medium",
     "• Capital 'C' followed by lowercase 'o' is elemental Cobalt (\\(\\text{Co}\\)); capital 'C' followed by capital 'O' denotes Carbon Monoxide (\\(\\text{CO}\\)).\nCorrect Choice is (B)."),

    # 510: Relative Mass of Chlorine Isotopes
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Fractional Atomic Mass of Chlorine</text>
  <!-- Cl-35 75% -->
  <rect x="35" y="55" width="190" height="40" fill="#3b82f6" rx="3"/>
  <text x="50" y="80" fill="#fff" font-size="11" font-weight="bold">³⁵Cl (75% Abundance)</text>
  <!-- Cl-37 25% -->
  <rect x="230" y="55" width="75" height="40" fill="#f59e0b" rx="3"/>
  <text x="235" y="80" fill="#0f172a" font-size="10" font-weight="bold">³⁷Cl (25%)</text>
  <!-- Weighted average calculation -->
  <text x="35" y="125" fill="#cbd5e1" font-size="10">Average Mass = (35 × 0.75) + (37 × 0.25)</text>
  <text x="35" y="145" fill="#cbd5e1" font-size="10">= 26.25 + 9.25 = 35.5 u</text>
  <rect x="35" y="165" width="270" height="35" fill="#1e293b" stroke="#34d399" rx="3"/>
  <text x="50" y="188" fill="#34d399" font-size="11" font-weight="bold">Standard Atomic Mass of Chlorine = 35.5 u</text>
</svg>
</div>
Why does Chlorine have a fractional relative atomic mass of \\(35.5\\text{ u}\\) when neutrons and protons only exist in whole numbers?""",
     ["Because individual chlorine nuclei contain half a neutron",
      "Because natural chlorine is a mixture of two isotopes (\\(^{35}\\text{Cl}\\) and \\(^{37}\\text{Cl}\\)) in a \\(3:1\\) natural abundance ratio, resulting in a weighted average of \\(35.5\\text{ u}\\)",
      "Because chlorine atoms lose mass when ionized",
      "Because electrons contribute \\(0.5\\text{ u}\\) to the mass"],
     "B", "OSC", "hard",
     "• Fractional atomic masses reflect the weighted average of naturally occurring stable isotopes: \\(\\frac{3 \\times 35 + 1 \\times 37}{4} = 35.5\\text{ u}\\).\nCorrect Choice is (B)."),

    # 511: Valency Chart of Common Metals & Nonmetals
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="95" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Valency Classification Grid</text>
  <!-- Monovalent -->
  <rect x="25" y="45" width="65" height="110" fill="#1e293b" stroke="#60a5fa" rx="3"/>
  <text x="30" y="65" fill="#93c5fd" font-size="9" font-weight="bold">Monovalent (1)</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="8">H⁺, Na⁺, K⁺</text>
  <text x="35" y="105" fill="#cbd5e1" font-size="8">Ag⁺, Cl⁻, F⁻</text>
  <!-- Divalent -->
  <rect x="100" y="45" width="65" height="110" fill="#1e293b" stroke="#34d399" rx="3"/>
  <text x="105" y="65" fill="#86efac" font-size="9" font-weight="bold">Divalent (2)</text>
  <text x="110" y="85" fill="#cbd5e1" font-size="8">Mg²⁺, Ca²⁺</text>
  <text x="110" y="105" fill="#cbd5e1" font-size="8">Zn²⁺, O²⁻</text>
  <!-- Trivalent -->
  <rect x="175" y="45" width="65" height="110" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="180" y="65" fill="#fde047" font-size="9" font-weight="bold">Trivalent (3)</text>
  <text x="185" y="85" fill="#cbd5e1" font-size="8">Al³⁺, Fe³⁺</text>
  <text x="185" y="105" fill="#cbd5e1" font-size="8">N³⁻, P³⁻</text>
  <!-- Tetravalent -->
  <rect x="250" y="45" width="65" height="110" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="253" y="65" fill="#fca5a5" font-size="8" font-weight="bold">Tetravalent (4)</text>
  <text x="260" y="85" fill="#cbd5e1" font-size="8">C⁴⁺, Si⁴⁺</text>
  <text x="260" y="105" fill="#cbd5e1" font-size="8">Pb⁴⁺</text>
  <text x="35" y="190" fill="#38bdf8" font-size="10">Valency corresponds to the ionic charge or shared bonds</text>
</svg>
</div>
Which of the following compounds is formed between a TRIVALENT metal cation and a DIVALENT nonmetal oxide anion?""",
     ["\\(\\text{NaCl}\\)", "\\(\\text{MgO}\\)", "\\(\\text{Al}_2\\text{O}_3\\)", "\\(\\text{CH}_4\\)"],
     "C", "OSC", "medium",
     "• In \\(\\text{Al}_2\\text{O}_3\\), Aluminium is trivalent (\\(\\text{Al}^{3+}\\)) and oxygen is divalent (\\(\\text{O}^{2-}\\)). Criss-cross valency yields \\(\\text{Al}_2\\text{O}_3\\).\nCorrect Choice is (C)."),

    # 512: Atomic Mass Spectrometry Mass-to-Charge Deflection
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Modern Mass Spectrometry Principle</text>
  <!-- Magnetic Field Region -->
  <rect x="120" y="60" width="100" height="90" fill="#1e293b" stroke="#6366f1" stroke-dasharray="4 4" rx="4"/>
  <text x="130" y="80" fill="#818cf8" font-size="10">Magnetic Field B</text>
  <!-- Ion Beam Entry -->
  <line x1="30" y1="105" x2="120" y2="105" stroke="#fde047" stroke-width="3"/>
  <text x="35" y="95" fill="#fde047" font-size="9">Ion Beam (q/m)</text>
  <!-- Deflection Paths -->
  <path d="M 120 105 Q 170 105 200 65" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="210" y="65" fill="#38bdf8" font-size="9">Lighter Ions (High Deflection)</text>
  <path d="M 120 105 Q 185 105 230 135" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <text x="210" y="150" fill="#f87171" font-size="9">Heavier Ions (Low Deflection)</text>
  <text x="45" y="195" fill="#cbd5e1" font-size="10">Radius of curvature r ∝ m/q allows exact atomic mass determination</text>
</svg>
</div>
How does a modern mass spectrometer determine the precise absolute mass of individual isotopes with extreme accuracy?""",
     ["By weighing millions of atoms on a microscopic spring balance",
      "By accelerating ionized atoms through a magnetic field, where the radius of curved path depends directly on the ion's mass-to-charge ratio (\\(m/q\\))",
      "By shining laser light and measuring reflected color",
      "By measuring how fast atoms sink in water"],
     "B", "OSC", "hard",
     "• In a magnetic field, centripetal force equals magnetic Lorentz force (\\(qvB = mv^2/r \\implies r = mv/qB\\)). Lighter ions curve sharply while heavier ions travel wider arcs, enabling exact isotopic mass measurement.\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-4-4.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-4-4.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-4-4.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch4_topic2.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
