import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced stoichiometric dissipation",
        "Passive thermodynamic stagnation",
        "Spontaneous non-stoichiometric dissociation"
    ]
    for d in default_distractors:
        if len(parts) >= 3:
            break
        if d not in parts:
            parts.append(d)
    return parts[:3]

def generate_vault_questions(topic_code, subtopic_name, archs):
    questions = []
    q_seq = 1

    for arch_idx, arch in enumerate(archs):
        templates = arch['templates']
        data_list = arch['data']
        calc_fn = arch['calc']
        diff = arch['diff']

        for i in range(10):
            template = templates[i % len(templates)]
            item = data_list[i % len(data_list)]

            correct_ans, wrong_choices, solution = calc_fn(item)
            q_text = template.format(*item)

            if q_seq <= 40:
                vault = 'exam'
            elif q_seq <= 60:
                vault = 'practice'
            else:
                vault = 'foundation'

            options_list = [
                {"id": "A", "text": correct_ans, "isCorrect": True},
                {"id": "B", "text": wrong_choices[0], "isCorrect": False},
                {"id": "C", "text": wrong_choices[1], "isCorrect": False},
                {"id": "D", "text": wrong_choices[2], "isCorrect": False}
            ]

            rot = (q_seq - 1) % 4
            shuffled_options = options_list[rot:] + options_list[:rot]
            labels = ["A", "B", "C", "D"]
            correct_letter = "A"
            final_options = []
            for idx, opt in enumerate(shuffled_options):
                lbl = labels[idx]
                is_corr = opt["isCorrect"]
                if is_corr:
                    correct_letter = lbl
                final_options.append({
                    "id": lbl,
                    "text": opt["text"],
                    "isCorrect": is_corr
                })

            q_code = f"{topic_code}-OSC-{q_seq:03d}"
            q_doc = {
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "difficulty": diff,
                "marks": 4,
                "negativeMarks": 1,
                "vault": vault,
                "topicCode": topic_code,
                "subtopic": topic_code,
                "chapterNumber": 9,
                "class": "9",
                "subjectCode": "SCIE",
                "boardCode": "CBSE",
                "type": "OSC",
                "solution": solution,
                "status": "approved"
            }
            questions.append(q_doc)
            q_seq += 1

    return questions

# ==============================================================================
# SUBTOPIC 9.2.3: Polyatomic ions and radicals (NH4+, SO4^2-, CO3^2-)
# ==============================================================================
def gen_9_2_3():
    archs = []

    # Arch 1: Definition of polyatomic ion
    archs.append({
        'templates': [
            "What is the definition of a polyatomic ion?",
            "How does a polyatomic ion differ from a simple monatomic ion?",
            "Which statement correctly describes a polyatomic ion in chemical nomenclature?",
            "A group of atoms carrying a net positive or negative electric charge is termed:"
        ],
        'data': [
            ("A cluster of atoms chemically bonded together that carries a net electric charge and behaves as a single unit", "A neutral molecule with zero dipole moment; A single atom with multiple electrons; An unbonded mixture of metal atoms"),
            ("A polyatomic ion contains multiple covalently bonded atoms carrying a net charge, whereas a monatomic ion consists of a single charged atom", "A polyatomic ion has no mass; Monatomic ions cannot participate in ionic bonding; Polyatomic ions only exist at 0 Kelvin"),
            ("It acts as a single indivisible charged entity in the formation of ionic compounds", "It spontaneously decomposes during crystal formation; It always has a neutral charge of zero; It cannot form salts with metals"),
            ("a polyatomic ion", "an isotope; a coordinate covalent bond; a neutral radical")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** An ion consisting of a single charged atom (such as \\(\\text{{Na}}^+\\), \\(\\text{{Cl}}^-\\), \\(\\text{{Mg}}^{{2+}}\\)) is called a monatomic ion.\\n\\n**Step 2:** A group of atoms carrying a net charge (positive or negative) that behaves as a single charged unit during chemical reactions is known as a polyatomic ion (e.g. \\(\\text{{NH}}_4^+\\), \\(\\text{{SO}}_4^{{2-}}\\), \\(\\text{{CO}}_3^{{2-}}\\)).\\n\\n**Step 3:** Correct definition is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Common monovalent polyatomic ions
    archs.append({
        'templates': [
            "What is the chemical formula and net charge of the {} ion?",
            "Which of the following polyatomic ions carries a net charge of {}?",
            "Identify the symbol and charge of the {} radical:",
            "What is the formula of {} ion?"
        ],
        'data': [
            ("Ammonium", "NH4⁺ (charge +1)", "-1; +2; -2", "+1"),
            ("Hydroxide", "OH⁻ (charge -1)", "+1; -2; -3", "-1"),
            ("Nitrate", "NO3⁻ (charge -1)", "+1; -2; -3", "-1"),
            ("Hydrogen carbonate (Bicarbonate)", "HCO3⁻ (charge -1)", "+1; -2; -3", "-1"),
            ("Ammonium", "NH4⁺", "NH3; NH2⁻; N³⁻", "+1"),
            ("Hydroxide", "OH⁻", "H2O; O²⁻; H⁺", "-1"),
            ("Nitrate", "NO3⁻", "NO2⁻; N³⁻; NO", "-1"),
            ("Bicarbonate", "HCO3⁻", "CO3²⁻; H2CO3; CO2", "-1")
        ],
        'calc': lambda item: (
            item[1],
            split_options(f"{item[2]}"),
            f"**Step 1:** Monovalent polyatomic ions carry a net unit charge (either +1 or -1).\\n\\n**Step 2:** The ammonium ion is the most common polyatomic cation: \\(\\text{{NH}}_4^+\\) (charge +1).\\n\\n**Step 3:** Common monovalent anions include hydroxide (\\(\\text{{OH}}^-\\)), nitrate (\\(\\text{{NO}}_3^-\\)), and hydrogen carbonate (\\(\\text{{HCO}}_3^-\\)). For {item[0]}, the formula and charge is {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Common divalent polyatomic ions
    archs.append({
        'templates': [
            "What is the chemical formula and charge of the {} ion?",
            "Which of the following is a divalent polyatomic anion carrying a -2 charge?",
            "What is the formula for the {} radical?",
            "The {} ion has the formula and valency:"
        ],
        'data': [
            ("Sulfate", "SO4²⁻ (valency 2)", "SO3²⁻; S²⁻; HSO4⁻"),
            ("Sulfite", "SO3²⁻ (valency 2)", "SO4²⁻; S²⁻; S2O3²⁻"),
            ("Carbonate", "CO3²⁻ (valency 2)", "HCO3⁻; C⁴⁻; CO2"),
            ("Sulfate", "SO4²⁻", "NO3⁻; PO4³⁻; Cl⁻"),
            ("Carbonate", "CO3²⁻", "OH⁻; NH4⁺; SO4²⁻ (distinct)"),
            ("Sulfite", "SO3²⁻", "SO4²⁻; NO2⁻; CO3²⁻")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** Divalent polyatomic ions carry a charge of -2 (valency 2).\\n\\n**Step 2:** Sulfate is \\(\\text{{SO}}_4^{{2-}}\\), Sulfite is \\(\\text{{SO}}_3^{{2-}}\\), and Carbonate is \\(\\text{{CO}}_3^{{2-}}\\).\\n\\n**Step 3:** For {item[0]}, the formula is {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 4: Trivalent polyatomic ion: Phosphate (PO4^3-)
    archs.append({
        'templates': [
            "What is the chemical formula, charge, and valency of the phosphate ion?",
            "Which of the following represents the phosphate polyatomic ion?",
            "What is the valency of the phosphate radical in chemical formula formulation?",
            "The phosphate ion PO4³⁻ carries how many units of negative charge?"
        ],
        'data': [
            ("PO4³⁻ (charge -3, valency 3)", "PO3³⁻; P³⁻; HPO4²⁻"),
            ("PO4³⁻", "PO3³⁻; P³⁻; PO4²⁻"),
            ("3", "1; 2; 4"),
            ("3 units of negative charge (-3)", "1 unit; 2 units; 4 units")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The phosphate ion is a trivalent polyatomic anion consisting of 1 phosphorus atom and 4 oxygen atoms.\\n\\n**Step 2:** It carries a net charge of -3: \\(\\text{{PO}}_4^{{3-}}\\).\\n\\n**Step 3:** Its valency in the criss-cross formulation is 3. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Counting total number of atoms in polyatomic ions and compounds
    archs.append({
        'templates': [
            "How many total atoms are present in a single {} ion?",
            "Determine the total number of constituent atoms in {}:",
            "What is the total atom count in one formula unit of {}?",
            "Calculate the total number of atoms present in {}:"
        ],
        'data': [
            ("phosphate (PO4³⁻)", 5, "1 P atom + 4 O atoms = 5 atoms", "4; 3; 6"),
            ("carbonate (CO3²⁻)", 4, "1 C atom + 3 O atoms = 4 atoms", "3; 5; 6"),
            ("ammonium (NH4⁺)", 5, "1 N atom + 4 H atoms = 5 atoms", "4; 6; 3"),
            ("sulfate (SO4²⁻)", 5, "1 S atom + 4 O atoms = 5 atoms", "4; 6; 3"),
            ("hydroxide (OH⁻)", 2, "1 O atom + 1 H atom = 2 atoms", "1; 3; 4"),
            ("nitrate (NO3⁻)", 4, "1 N atom + 3 O atoms = 4 atoms", "3; 5; 2"),
            ("ammonium carbonate (NH4)2CO3", 14, "2 N + 8 H + 1 C + 3 O = 14 atoms", "12; 10; 16"),
            ("aluminium sulfate Al2(SO4)3", 17, "2 Al + 3 S + 12 O = 17 atoms", "14; 15; 20")
        ],
        'calc': lambda item: (
            f"{item[1]} atoms",
            split_options(item[3]),
            f"**Step 1:** Count the number of each type of atom present in the chemical formula.\\n\\n**Step 2:** For {item[0]}: {item[2]}.\\n\\n**Step 3:** Total number of atoms = {item[1]} atoms."
        ),
        'diff': 'medium'
    })

    # Arch 6: Monatomic vs Polyatomic ion classification
    archs.append({
        'templates': [
            "Classify the following ions: Na⁺, NH4⁺, Cl⁻, SO4²⁻. Which pair represents polyatomic ions?",
            "Which of the following is a MONATOMIC ion rather than a polyatomic ion?",
            "Which of the following contains ONLY polyatomic ions?",
            "Identify the polyatomic cation among the following species:"
        ],
        'data': [
            ("NH4⁺ and SO4²⁻", "Na⁺ and Cl⁻; Na⁺ and SO4²⁻; NH4⁺ and Cl⁻"),
            ("Sulfide ion (S²⁻)", "Sulfate ion (SO4²⁻); Sulfite ion (SO3²⁻); Carbonate ion (CO3²⁻)"),
            ("Nitride ion (N³⁻)", "Nitrate ion (NO3⁻); Nitrite ion (NO2⁻); Ammonium ion (NH4⁺)"),
            ("Chloride ion (Cl⁻)", "Hydroxide ion (OH⁻); Bicarbonate ion (HCO3⁻); Phosphate ion (PO4³⁻)"),
            ("Ammonium ion (NH4⁺)", "Hydronium ion is also polyatomic; Sodium ion (Na⁺); Potassium ion (K⁺); Calcium ion (Ca²⁺)")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Monatomic ions consist of a single charged atom (e.g., \\(\\text{{S}}^{{2-}}, \\text{{N}}^{{3-}}, \\text{{Cl}}^-, \\text{{Na}}^+\\)).\\n\\n**Step 2:** Polyatomic ions consist of two or more covalently bonded atoms carrying an overall net charge (e.g., \\(\\text{{NH}}_4^+, \\text{{SO}}_4^{{2-}}, \\text{{NO}}_3^-\\)).\\n\\n**Step 3:** Correct classification is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Parentheses convention for polyatomic ions
    archs.append({
        'templates': [
            "When writing the chemical formula of an ionic compound containing a polyatomic ion, why are brackets (parentheses) used when the subscript is greater than 1?",
            "In the formula of magnesium hydroxide Mg(OH)2, what do the brackets around OH indicate?",
            "Why is the formula of aluminium sulfate written as Al2(SO4)3 rather than Al2SO43?",
            "Which of the following formulas correctly uses parentheses for a polyatomic ion?"
        ],
        'data': [
            ("To indicate that the subscript multiplier applies to the entire group of atoms in the polyatomic ion", "To indicate the valency of the metal; To show that the compound is covalent; To separate positive and negative charges"),
            ("There are two complete hydroxide (OH) groups bound to each magnesium ion (total 2 O and 2 H)", "The hydrogen atom is squared; Magnesium is bound only to oxygen; The compound is a gas"),
            ("Without brackets, 43 would indicate 43 oxygen atoms rather than 3 sulfate groups", "Aluminium cannot bond without brackets; Sulfate has zero charge; Because sulfur is volatile"),
            ("Ca(OH)2", "CaOH2; Ca(OH); Ca2OH")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In chemical formulas, if a compound contains more than one unit of a polyatomic ion, the polyatomic ion must be enclosed in brackets with the subscript outside.\\n\\n**Step 2:** For example, \\(\\text{{Mg(OH)}}_2\\) signifies that there are two \\(\\text{{OH}}^-\\) ions per \\(\\text{{Mg}}^{{2+}}\\) ion (giving 2 O and 2 H atoms).\\n\\n**Step 3:** Writing \\(\\text{{MgOH}}_2\\) would incorrectly indicate 1 Mg, 1 O, and 2 H atoms. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Distinguishing sulfide (S^2-), sulfite (SO3^2-), and sulfate (SO4^2-)
    archs.append({
        'templates': [
            "What are the chemical formulas and names for the sulfur-containing anions: sulfide, sulfite, and sulfate?",
            "Which anion has the formula SO3²⁻?",
            "Which anion has the formula S²⁻?",
            "What is the difference in oxygen atoms between a sulfate ion and a sulfite ion?"
        ],
        'data': [
            ("Sulfide = S²⁻, Sulfite = SO3²⁻, Sulfate = SO4²⁻", "Sulfide = SO4²⁻, Sulfite = S²⁻, Sulfate = SO3²⁻; Sulfide = SO3²⁻, Sulfite = SO4²⁻, Sulfate = S²⁻; All three are identical"),
            ("Sulfite ion", "Sulfate ion; Sulfide ion; Thiosulfate ion"),
            ("Sulfide ion", "Sulfite ion; Sulfate ion; Persulfate ion"),
            ("Sulfate has 4 oxygen atoms while sulfite has 3 oxygen atoms (difference of 1 oxygen atom)", "Sulfate has 2 more oxygens than sulfite; Sulfite has 4 oxygens while sulfate has 3; Sulfate has no oxygen atoms")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sulfide is the simple monatomic anion formed by sulfur: \\(\\text{{S}}^{{2-}}\\).\\n\\n**Step 2:** Sulfite is the polyatomic oxyanion with 3 oxygens: \\(\\text{{SO}}_3^{{2-}}\\).\\n\\n**Step 3:** Sulfate is the polyatomic oxyanion with 4 oxygens: \\(\\text{{SO}}_4^{{2-}}\\). Correct distinction is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-9-9.2.3', 'Polyatomic ions and radicals (NH4+, SO4^2-, CO3^2-)', archs)

# ==============================================================================
# SUBTOPIC 9.3.1: Criss-cross valency method for ionic and covalent compounds
# ==============================================================================
def gen_9_3_1():
    archs = []

    # Arch 1: Criss-cross method principles
    archs.append({
        'templates': [
            "What is the fundamental principle of the criss-cross method for writing chemical formulas?",
            "When writing the formula of an ionic compound, which component is written first by convention?",
            "If the interchanged valencies of two combining elements share a common factor (e.g. 2 and 2, or 2 and 4), how should the formula be simplified?",
            "In writing chemical formulas, the total positive charge and total negative charge in a formula unit must:"
        ],
        'data': [
            ("The valencies or charges of the combining species are transposed as subscripts to the opposite partner and simplified to the lowest whole-number ratio", "Valencies are multiplied together; Valencies are added to atomic numbers; Subscripts are written in alphabetical order"),
            ("The positive ion (cation / metal) is written first, followed by the negative ion (anion / non-metal)", "The anion is written first; The element with higher mass is written first; The element with more letters is written first"),
            ("The subscripts are divided by their greatest common divisor to obtain the simplest empirical formula", "The subscripts are kept as large as possible; The subscripts are multiplied by 2; The compound is written as two separate words"),
            ("balance each other exactly so that the overall formula unit is electrically neutral", "equal +1 always; be greater than zero; equal the sum of atomic numbers")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In the criss-cross method, symbols of combining ions are written with their valencies below them.\\n\\n**Step 2:** The valencies are crossed over and written as subscripts of the other atom.\\n\\n**Step 3:** The subscripts are simplified to the lowest whole-number ratio to ensure overall electrical neutrality. Correct statement is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Binary simple covalent and ionic compounds
    archs.append({
        'templates': [
            "Using the criss-cross method, what is the chemical formula of {}?",
            "What is the chemical formula formed between {} (valency {}) and {} (valency {})?",
            "Determine the correct formula for {}:",
            "Which of the following is the correct chemical formula of {}?"
        ],
        'data': [
            ("Hydrogen chloride", "Hydrogen", 1, "Chlorine", 1, "HCl", "H2Cl; HCl2; H2Cl2"),
            ("Hydrogen sulfide", "Hydrogen", 1, "Sulfur", 2, "H2S", "HS; HS2; H2S2"),
            ("Water", "Hydrogen", 1, "Oxygen", 2, "H2O", "HO; HO2; H2O2"),
            ("Ammonia", "Nitrogen", 3, "Hydrogen", 1, "NH3", "N3H; NH; N2H3"),
            ("Carbon tetrachloride", "Carbon", 4, "Chlorine", 1, "CCl4", "C4Cl; CCl; C2Cl4"),
            ("Magnesium chloride", "Magnesium", 2, "Chlorine", 1, "MgCl2", "Mg2Cl; MgCl; Mg2Cl3"),
            ("Aluminium oxide", "Aluminium", 3, "Oxygen", 2, "Al2O3", "Al3O2; AlO; AlO2"),
            ("Calcium oxide", "Calcium", 2, "Oxygen", 2, "CaO", "Ca2O2; CaO2; Ca2O")
        ],
        'calc': lambda item: (
            item[5],
            split_options(item[6]),
            f"**Step 1:** Write the symbols of {item[1]} and {item[3]} with their valencies: {item[1]} has valency {item[2]}, {item[3]} has valency {item[4]}.\\n\\n**Step 2:** Criss-cross the valencies: the valency of {item[3]} becomes the subscript of {item[1]}, and the valency of {item[1]} becomes the subscript of {item[3]}.\\n\\n**Step 3:** Simplifying to the simplest whole-number ratio gives {item[5]}. Correct formula is {item[5]}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Formula of compounds with simple polyatomic ions
    archs.append({
        'templates': [
            "What is the correct chemical formula of {}?",
            "Using the criss-cross method, determine the formula of {} formed by cation and anion:",
            "Which formula correctly represents {}?",
            "Determine the formula of {} containing polyatomic ions:"
        ],
        'data': [
            ("Sodium nitrate", "NaNO3", "Na(NO3)2; Na2NO3; Na3N"),
            ("Calcium hydroxide", "Ca(OH)2", "CaOH2; Ca2OH; Ca(OH)"),
            ("Sodium carbonate", "Na2CO3", "NaCO3; Na(CO3)2; Na2(CO3)3"),
            ("Calcium carbonate", "CaCO3", "Ca2CO3; Ca(CO3)2; Ca2(CO3)2"),
            ("Magnesium hydroxide", "Mg(OH)2", "MgOH2; Mg2OH; Mg(OH)"),
            ("Sodium hydroxide", "NaOH", "Na(OH)2; Na2OH; NaO2H"),
            ("Potassium nitrate", "KNO3", "K2NO3; K(NO3)2; K3N"),
            ("Calcium sulfate", "CaSO4", "Ca2SO4; Ca(SO4)2; Ca2(SO4)2")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** Identify the constituent cation and anion and their respective valencies.\\n\\n**Step 2:** Criss-cross the valencies. If the subscript of a polyatomic ion is greater than 1, enclose it in brackets.\\n\\n**Step 3:** For {item[0]}, the correct chemical formula is {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Advanced polyatomic combinations
    archs.append({
        'templates': [
            "What is the chemical formula of {}?",
            "Determine the correct formula for {}:",
            "Using the criss-cross method for {} (cation valency {} and anion valency {}):",
            "Which of the following represents the correct formula of {}?"
        ],
        'data': [
            ("Aluminium sulfate", "Al2(SO4)3", "Al3(SO4)2; AlSO4; Al2SO43"),
            ("Ammonium sulfate", "(NH4)2SO4", "NH4SO4; (NH4)2(SO4)2; NH4(SO4)2"),
            ("Ammonium carbonate", "(NH4)2CO3", "NH4CO3; (NH4)3CO2; NH4(CO3)2"),
            ("Aluminium hydroxide", "Al(OH)3", "Al3OH; AlOH3; Al(OH)2"),
            ("Calcium phosphate", "Ca3(PO4)2", "Ca2(PO4)3; CaPO4; Ca3PO42"),
            ("Magnesium phosphate", "Mg3(PO4)2", "Mg2(PO4)3; MgPO4; Mg3PO42"),
            ("Ammonium phosphate", "(NH4)3PO4", "NH4PO4; (NH4)2PO4; NH4(PO4)3"),
            ("Sodium bicarbonate", "NaHCO3", "Na2HCO3; Na(HCO3)2; Na2CO3")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** Identify the ions and their valencies for {item[0]}.\\n\\n**Step 2:** Transpose the valencies as subscripts for each partner, placing polyatomic ions inside brackets when subscript > 1.\\n\\n**Step 3:** The correct formula is {item[1]}."
        ),
        'diff': 'hard'
    })

    # Arch 5: Criss-cross deduction for generalized elements X and Y
    archs.append({
        'templates': [
            "An element X has valency {} and element Y has valency {}. What is the formula of the compound formed between X and Y?",
            "If metal M forms an ion M^{{n+}} with valency {} and non-metal X forms X^{{m-}} with valency {}, the resulting chemical formula is:",
            "What formula results when element A (valency {}) combines with element B (valency {})?",
            "Element P has valency {} and element Q has valency {}. The chemical formula of their compound is:"
        ],
        'data': [
            (3, 2, "X2Y3", "X3Y2; XY; XY3"),
            (1, 2, "X2Y", "XY2; XY; X2Y2"),
            (2, 1, "XY2", "X2Y; XY; X2Y2"),
            (1, 1, "XY", "X2Y; XY2; X2Y2"),
            (2, 2, "XY", "X2Y2; XY2; X2Y"),
            (3, 1, "XY3", "X3Y; X2Y3; XY"),
            (4, 2, "XY2", "X2Y4; X4Y2; XY"),
            (3, 3, "XY", "X3Y3; X2Y3; XY3")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** Symbols: X has valency {item[0]} and Y has valency {item[1]}.\\n\\n**Step 2:** Transpose valencies: X receives subscript {item[1]} and Y receives subscript {item[0]}.\\n\\n**Step 3:** Simplifying the subscripts to lowest whole numbers gives {item[2]}."
        ),
        'diff': 'medium'
    })

    # Arch 6: Naming of binary ionic and covalent compounds
    archs.append({
        'templates': [
            "What is the IUPAC name of the compound with chemical formula {}?",
            "What is the name of the binary compound {}?",
            "How is the compound {} correctly named?",
            "Name the chemical compound represented by {}:"
        ],
        'data': [
            ("FeCl2", "Iron(II) chloride (Ferrous chloride)", "Iron(III) chloride; Iron chloride; Ferric chloride"),
            ("FeCl3", "Iron(III) chloride (Ferric chloride)", "Iron(II) chloride; Ferrous chloride; Iron trichloride"),
            ("Cu2O", "Copper(I) oxide (Cuprous oxide)", "Copper(II) oxide; Cupric oxide; Copper dioxide"),
            ("CuO", "Copper(II) oxide (Cupric oxide)", "Copper(I) oxide; Cuprous oxide; Copper suboxide"),
            ("CO", "Carbon monoxide", "Carbon dioxide; Carbonic acid; Monocarbon oxide"),
            ("CO2", "Carbon dioxide", "Carbon monoxide; Carbon trioxide; Dicarbon oxide"),
            ("SO2", "Sulfur dioxide", "Sulfur trioxide; Sulfur oxide; Monosulfur dioxide"),
            ("SO3", "Sulfur trioxide", "Sulfur dioxide; Sulfuric acid; Sulfate")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** For transition metals showing variable valency, the oxidation state / valency is indicated in Roman numerals in parentheses (Stock notation).\\n\\n**Step 2:** For covalent compounds, prefixes like mono-, di-, tri- indicate the number of atoms.\\n\\n**Step 3:** For {item[0]}, the correct name is {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 7: Correcting faulty chemical formulas
    archs.append({
        'templates': [
            "A student writes the formula of calcium hydroxide as CaOH2. Why is this formula scientifically INCORRECT, and what is the correct formula?",
            "Why is the formula of magnesium nitrate written as Mg(NO3)2 rather than MgNO32?",
            "Identify the INCORRECT chemical formula among the following:",
            "Which of the following represents a correct chemical formula?"
        ],
        'data': [
            ("It is incorrect because without brackets, 2 applies only to hydrogen; correct formula is Ca(OH)2", "It is correct as written; Calcium has valency 1; Oxygen cannot form bonds with calcium"),
            ("Without brackets, 32 would denote thirty-two oxygen atoms; correct formula is Mg(NO3)2", "Magnesium has valency 3; Nitrate has -2 charge; Brackets are optional"),
            ("AlSO4 (incorrect; correct is Al2(SO4)3)", "NaCl; CaCO3; H2O"),
            ("Al2(SO4)3", "AlSO4; Al3(SO4)2; Al2SO4")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A polyatomic ion must be enclosed in brackets whenever its subscript is 2 or greater.\\n\\n**Step 2:** Writing \\(\\text{{CaOH}}_2\\) means 1 Ca, 1 O, and 2 H, which violates stoichiometry.\\n\\n**Step 3:** The correct formula is \\(\\text{{Ca(OH)}}_2\\). Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Determining valency of unknown element M from compound formula
    archs.append({
        'templates': [
            "An element M forms an oxide with formula {}. What is the valency of element M?",
            "If the chloride of a metal M has the formula {}, what is the valency of M?",
            "A metal M forms a sulfate with formula {}. What is the valency of metal M?",
            "The formula of the phosphate of an element M is {}. Determine the valency of M:"
        ],
        'data': [
            ("M2O3", 3, "Since oxygen has valency 2, M must have valency 3", "1; 2; 4"),
            ("MO", 2, "Since oxygen has valency 2, M must have valency 2", "1; 3; 4"),
            ("M2O", 1, "Since oxygen has valency 2, M must have valency 1", "2; 3; 4"),
            ("MCl3", 3, "Since chlorine has valency 1, M must have valency 3", "1; 2; 4"),
            ("MCl2", 2, "Since chlorine has valency 1, M must have valency 2", "1; 3; 4"),
            ("M(SO4)2", 4, "Since sulfate has valency 2, M must have valency 4", "1; 2; 3"),
            ("MSO4", 2, "Since sulfate has valency 2, M must have valency 2", "1; 3; 4"),
            ("MPO4", 3, "Since phosphate has valency 3, M must have valency 3", "1; 2; 4")
        ],
        'calc': lambda item: (
            str(item[1]),
            split_options(item[3]),
            f"**Step 1:** In a compound formula \\(\\text{{M}}_x\\text{{X}}_y\\), the ratio of valencies is \\(\\text{{valency of M}} : \\text{{valency of X}} = y : x\\).\\n\\n**Step 2:** For {item[0]}: {item[2]}.\\n\\n**Step 3:** Therefore, the valency of M is {item[1]}."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-9-9.3.1', 'Criss-cross valency method for ionic and covalent compounds', archs)

# ==============================================================================
# SUBTOPIC 9.3.2: Calculating molecular mass and formula unit mass in unified atomic mass units (u)
# ==============================================================================
def gen_9_3_2():
    archs = []

    # Arch 1: Definition of molecular mass vs formula unit mass
    archs.append({
        'templates': [
            "What is the definition of the molecular mass of a substance?",
            "What is the difference between the molecular mass and the formula unit mass of a substance?",
            "Why is the term 'formula unit mass' used for sodium chloride (NaCl) instead of 'molecular mass'?",
            "How is the molecular mass of a chemical compound calculated?"
        ],
        'data': [
            ("The sum of the atomic masses of all the atoms present in a single molecule of the substance", "The mass of one mole of substance in kilograms; The mass of the nucleus only; The product of atomic numbers"),
            ("Both are calculated by summing atomic masses, but molecular mass is used for discrete molecules while formula unit mass is used for ionic lattice compounds", "Formula unit mass has no units; Molecular mass is only measured in grams; Formula unit mass applies only to gases"),
            ("Because sodium chloride does not exist as discrete neutral molecules but as a continuous 3D crystalline lattice of ions", "Because sodium is radioactive; Because NaCl has no mass; Because chlorine is an inert gas"),
            ("By multiplying the atomic mass of each element by the number of its atoms in the formula and summing all values", "By subtracting atomic numbers from mass numbers; By averaging the atomic masses; By dividing by Avogadro's number")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The molecular mass of a substance is the sum of the atomic masses of all the atoms in a molecule of the substance.\\n\\n**Step 2:** The formula unit mass is calculated in exactly the same manner, but the term is preferred for ionic substances (like \\(\\text{{NaCl}}, \\text{{CaCl}}_2\\)) whose constituent particles are ions rather than discrete molecules.\\n\\n**Step 3:** Both are expressed in unified atomic mass units (u). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Molecular mass of common simple gases/molecules
    archs.append({
        'templates': [
            "Calculate the molecular mass of {} (atomic masses: {}):",
            "What is the molecular mass of {} in unified atomic mass units (u)?",
            "Determine the molecular mass of {}:",
            "The molecular mass of {} is calculated to be:"
        ],
        'data': [
            ("Hydrogen gas (H2)", "H = 1 u", "2 u", "1 u; 4 u; 0.5 u"),
            ("Oxygen gas (O2)", "O = 16 u", "32 u", "16 u; 48 u; 64 u"),
            ("Chlorine gas (Cl2)", "Cl = 35.5 u", "71 u", "35.5 u; 70 u; 72 u"),
            ("Carbon dioxide (CO2)", "C = 12 u, O = 16 u", "44 u", "28 u; 32 u; 56 u"),
            ("Methane (CH4)", "C = 12 u, H = 1 u", "16 u", "14 u; 18 u; 20 u"),
            ("Ethane (C2H6)", "C = 12 u, H = 1 u", "30 u", "28 u; 32 u; 34 u"),
            ("Ethene (C2H4)", "C = 12 u, H = 1 u", "28 u", "26 u; 30 u; 32 u"),
            ("Ammonia (NH3)", "N = 14 u, H = 1 u", "17 u", "15 u; 18 u; 16 u")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** Identify the atoms in the formula: {item[0]}.\\n\\n**Step 2:** Sum the atomic masses of all constituent atoms using {item[1]}.\\n\\n**Step 3:** Molecular mass = {item[2]}. Correct answer is {item[2]}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Molecular mass of water, hydrogen peroxide, ozone, and sulfur dioxide
    archs.append({
        'templates': [
            "Calculate the molecular mass of {} (atomic masses: {}):",
            "What is the molecular mass of {}?",
            "Determine the molecular mass of {}:",
            "The mass of one molecule of {} in unified atomic mass units (u) is:"
        ],
        'data': [
            ("Water (H2O)", "H = 1 u, O = 16 u", "18 u", "16 u; 20 u; 17 u"),
            ("Hydrogen peroxide (H2O2)", "H = 1 u, O = 16 u", "34 u", "18 u; 32 u; 36 u"),
            ("Ozone (O3)", "O = 16 u", "48 u", "32 u; 16 u; 64 u"),
            ("Sulfur dioxide (SO2)", "S = 32 u, O = 16 u", "64 u", "48 u; 80 u; 32 u"),
            ("Sulfur trioxide (SO3)", "S = 32 u, O = 16 u", "80 u", "64 u; 96 u; 48 u"),
            ("Methanol (CH3OH)", "C = 12 u, H = 1 u, O = 16 u", "32 u", "30 u; 34 u; 28 u"),
            ("Ethanol (C2H5OH)", "C = 12 u, H = 1 u, O = 16 u", "46 u", "44 u; 48 u; 42 u"),
            ("Glucose (C6H12O6)", "C = 12 u, H = 1 u, O = 16 u", "180 u", "160 u; 190 u; 200 u")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** List the constituent atoms and their counts in {item[0]}.\\n\\n**Step 2:** Multiply atom counts by atomic masses ({item[1]}).\\n\\n**Step 3:** Total molecular mass = {item[2]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Formula unit mass of ionic compounds
    archs.append({
        'templates': [
            "Calculate the formula unit mass of {} (atomic masses: {}):",
            "What is the formula unit mass of {}?",
            "Determine the formula unit mass of {}:",
            "The formula unit mass of {} in unified atomic mass units (u) is:"
        ],
        'data': [
            ("Sodium chloride (NaCl)", "Na = 23 u, Cl = 35.5 u", "58.5 u", "57.5 u; 59.5 u; 58.0 u"),
            ("Calcium chloride (CaCl2)", "Ca = 40 u, Cl = 35.5 u", "111 u", "75.5 u; 110 u; 112 u"),
            ("Magnesium oxide (MgO)", "Mg = 24 u, O = 16 u", "40 u", "24 u; 38 u; 42 u"),
            ("Zinc oxide (ZnO)", "Zn = 65 u, O = 16 u", "81 u", "65 u; 80 u; 82 u"),
            ("Potassium carbonate (K2CO3)", "K = 39 u, C = 12 u, O = 16 u", "138 u", "120 u; 140 u; 136 u"),
            ("Sodium carbonate (Na2CO3)", "Na = 23 u, C = 12 u, O = 16 u", "106 u", "83 u; 104 u; 108 u"),
            ("Calcium carbonate (CaCO3)", "Ca = 40 u, C = 12 u, O = 16 u", "100 u", "98 u; 102 u; 90 u"),
            ("Sodium hydroxide (NaOH)", "Na = 23 u, O = 16 u, H = 1 u", "40 u", "39 u; 41 u; 42 u")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** The formula unit mass is calculated by adding the atomic masses of all atoms present in one formula unit.\\n\\n**Step 2:** For {item[0]}: {item[1]}.\\n\\n**Step 3:** Total formula unit mass = {item[2]}."
        ),
        'diff': 'easy'
    })

    # Arch 5: Molecular mass of common oxyacids
    archs.append({
        'templates': [
            "Calculate the molecular mass of {} (atomic masses: {}):",
            "What is the molecular mass of {}?",
            "Determine the molecular mass of {}:",
            "The molecular mass of {} is calculated as:"
        ],
        'data': [
            ("Nitric acid (HNO3)", "H = 1 u, N = 14 u, O = 16 u", "63 u", "62 u; 64 u; 65 u"),
            ("Sulfuric acid (H2SO4)", "H = 1 u, S = 32 u, O = 16 u", "98 u", "96 u; 100 u; 94 u"),
            ("Carbonic acid (H2CO3)", "H = 1 u, C = 12 u, O = 16 u", "62 u", "60 u; 64 u; 63 u"),
            ("Phosphoric acid (H3PO4)", "H = 1 u, P = 31 u, O = 16 u", "98 u", "96 u; 100 u; 95 u"),
            ("Hydrochloric acid (HCl)", "H = 1 u, Cl = 35.5 u", "36.5 u", "35.5 u; 37.5 u; 36.0 u"),
            ("Acetic acid / Ethanoic acid (CH3COOH)", "C = 12 u, H = 1 u, O = 16 u", "60 u", "58 u; 62 u; 64 u")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** Write the constituent atoms for {item[0]}.\\n\\n**Step 2:** Calculate total mass: multiply atom counts by atomic masses given in {item[1]}.\\n\\n**Step 3:** Total molecular mass = {item[2]}."
        ),
        'diff': 'medium'
    })

    # Arch 6: Formula unit mass of hydrated salts
    archs.append({
        'templates': [
            "Calculate the formula unit mass of {} (atomic masses: {}):",
            "What is the formula unit mass of {}?",
            "Determine the mass of one formula unit of hydrated {}:",
            "The formula unit mass of {} is calculated as:"
        ],
        'data': [
            ("Copper sulfate pentahydrate (CuSO4 · 5H2O)", "Cu = 63.5 u, S = 32 u, O = 16 u, H = 1 u", "249.5 u", "159.5 u; 250.0 u; 248.5 u"),
            ("Washing soda (Na2CO3 · 10H2O)", "Na = 23 u, C = 12 u, O = 16 u, H = 1 u", "286 u", "106 u; 284 u; 288 u"),
            ("Gypsum (CaSO4 · 2H2O)", "Ca = 40 u, S = 32 u, O = 16 u, H = 1 u", "172 u", "136 u; 170 u; 174 u"),
            ("Plaster of Paris (CaSO4 · 0.5H2O)", "Ca = 40 u, S = 32 u, O = 16 u, H = 1 u", "145 u", "136 u; 144 u; 146 u"),
            ("Ferrous sulfate heptahydrate (FeSO4 · 7H2O)", "Fe = 56 u, S = 32 u, O = 16 u, H = 1 u", "278 u", "152 u; 276 u; 280 u"),
            ("Magnesium sulfate heptahydrate (Epsom salt, MgSO4 · 7H2O)", "Mg = 24 u, S = 32 u, O = 16 u, H = 1 u", "246 u", "120 u; 244 u; 248 u")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** A hydrated salt contains water of crystallization. The mass of water molecules (\\(18\\text{{ u}}\\) per \\(\\text{{H}}_2\\text{{O}}\\)) must be added to the anhydrous salt mass.\\n\\n**Step 2:** Calculate anhydrous salt mass + \\(n \\times 18\\text{{ u}}\\).\\n\\n**Step 3:** Total formula unit mass for {item[0]} = {item[2]}."
        ),
        'diff': 'hard'
    })

    # Arch 7: Percentage composition of elements by mass
    archs.append({
        'templates': [
            "Calculate the percentage of {} in {} (molecular mass = {} u):",
            "What is the mass percentage of {} in {}?",
            "Determine the percentage composition of {} in {}:",
            "The percentage of {} by mass in {} is:"
        ],
        'data': [
            ("Oxygen", "water (H2O)", 18, "88.9%", "11.1%; 50.0%; 80.0%"),
            ("Hydrogen", "water (H2O)", 18, "11.1%", "88.9%; 5.5%; 20.0%"),
            ("Carbon", "carbon dioxide (CO2)", 44, "27.3%", "72.7%; 30.0%; 25.0%"),
            ("Oxygen", "carbon dioxide (CO2)", 44, "72.7%", "27.3%; 70.0%; 75.0%"),
            ("Nitrogen", "ammonia (NH3)", 17, "82.4%", "17.6%; 80.0%; 85.0%"),
            ("Hydrogen", "ammonia (NH3)", 17, "17.6%", "82.4%; 15.0%; 20.0%"),
            ("Calcium", "calcium carbonate (CaCO3)", 100, "40.0%", "12.0%; 48.0%; 50.0%"),
            ("Carbon", "calcium carbonate (CaCO3)", 100, "12.0%", "40.0%; 48.0%; 10.0%"),
            ("Oxygen", "calcium carbonate (CaCO3)", 100, "48.0%", "40.0%; 12.0%; 50.0%")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[4]),
            f"**Step 1:** Formula: \\(\\text{{Mass percentage}} = \\frac{{\\text{{Total mass of element in formula}}}}{{\\text{{Molecular / Formula mass}}}} \\times 100\\).\\n\\n**Step 2:** For {item[0]} in {item[1]}: numerator is the contribution of {item[0]} and denominator is {item[2]} u.\\n\\n**Step 3:** The percentage is {item[3]}."
        ),
        'diff': 'medium'
    })

    # Arch 8: Determining unknown atomic mass of an element X from compound formula mass
    archs.append({
        'templates': [
            "A compound has formula {} and formula unit mass {} u. If atomic mass of O = 16 u, what is the atomic mass of element X?",
            "The molecular mass of {} is {} u. Given atomic masses: H = 1 u, O = 16 u, find the atomic mass of element X:",
            "An oxide of a trivalent metal has formula {} and formula unit mass {} u. What is the atomic mass and identity of element X?",
            "The formula unit mass of {} is {} u. If Cl = 35.5 u, what is the atomic mass of metal X?"
        ],
        'data': [
            ("X2O3", 102, 27, "Aluminium (27 u)", "24 u; 28 u; 31 u"),
            ("X2O", 62, 23, "Sodium (23 u)", "19 u; 24 u; 39 u"),
            ("XO", 56, 40, "Calcium (40 u)", "24 u; 56 u; 65 u"),
            ("XO2", 44, 12, "Carbon (12 u)", "14 u; 28 u; 32 u"),
            ("XCl", 58.5, 23, "Sodium (23 u)", "39 u; 24 u; 27 u"),
            ("XCl2", 111, 40, "Calcium (40 u)", "24 u; 56 u; 65 u"),
            ("XCl3", 133.5, 27, "Aluminium (27 u)", "31 u; 56 u; 24 u")
        ],
        'calc': lambda item: (
            f"{item[2]} u",
            split_options(item[4]),
            f"**Step 1:** Set up the formula unit mass equation for {item[0]}: \\(\\text{{Total Mass}} = \\sum \\text{{atomic masses}} = {item[1]}\\text{{ u}}\\).\\n\\n**Step 2:** Subtract the known masses of the other atoms and divide by the number of X atoms.\\n\\n**Step 3:** The atomic mass of element X is {item[2]} u ({item[3]})."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-9-9.3.2', 'Calculating molecular mass and formula unit mass in unified atomic mass units (u)', archs)

def main():
    all_questions = []

    print("Generating 9.2.3...")
    q_9_2_3 = gen_9_2_3()
    print(f"9.2.3 generated {len(q_9_2_3)} questions")
    all_questions.extend(q_9_2_3)

    print("Generating 9.3.1...")
    q_9_3_1 = gen_9_3_1()
    print(f"9.3.1 generated {len(q_9_3_1)} questions")
    all_questions.extend(q_9_3_1)

    print("Generating 9.3.2...")
    q_9_3_2 = gen_9_3_2()
    print(f"9.3.2 generated {len(q_9_3_2)} questions")
    all_questions.extend(q_9_3_2)

    out_file = 'scripts/cbse9_scie_ch9_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
